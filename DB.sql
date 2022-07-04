CREATE TABLE "public.pqr_radicacions" (
	"id" serial NOT NULL,
	"glb_estado_id" int NOT NULL,
	"glb_dependencia_id" int NOT NULL,
	"pqr_derechos_id" int NOT NULL,
	"ase_tipo_poblacion_id" int NOT NULL,
	"ase_tipo_regimen_id" int,
	"pqr_tipo_solicitud_id" int NOT NULL,
	"pqr_tipo_solicitud_especifica_id" int NOT NULL,
	"glb_barrio_vereda" int NOT NULL,
	"glb_tipo_identificacion_id" int NOT NULL,
	"identificacion" character varying NOT NULL,
	"primer_apellido" character varying,
	"segundo_apellido" character varying,
	"primer_nombre" character varying,
	"segundo_nombre" character varying,
	"direccion" character varying(256),
	"telefono_fijo" character varying(7),
	"telefono_movil" character varying(10),
	"email" character varying,
	"ficha_sisben" character varying,
	"clasificacion_sisben" character varying,
	"no_radicacion" character varying,
	"fecha_radicacion" DATE NOT NULL,
	"fecha_vencimiento" DATE NOT NULL,
	"no_respuesta" character varying,
	"asunto" character varying(1500) NOT NULL,
	"otros_tipo_solicitud_esp" character varying,
	"amisalud_id" character varying,
	"nombre_completo" character varying,
	"fecha_nacimiento" DATE,
	CONSTRAINT "pqr_radicacions_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.pqr_tipo_solicituds" (
	"id" int NOT NULL,
	"descripcion" character varying NOT NULL UNIQUE,
	CONSTRAINT "pqr_tipo_solicituds_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.glb_estados" (
	"id" int NOT NULL,
	"descripcion" character varying NOT NULL UNIQUE,
	CONSTRAINT "glb_estados_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.glb_dependencias" (
	"id" int NOT NULL,
	"descripcion" character varying NOT NULL UNIQUE,
	CONSTRAINT "glb_dependencias_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.pqr_tipo_derechos" (
	"id" int NOT NULL,
	"descripcion" character varying NOT NULL UNIQUE,
	CONSTRAINT "pqr_tipo_derechos_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.ase_tipo_poblacions" (
	"id" int NOT NULL,
	"descripcion" character varying NOT NULL UNIQUE,
	CONSTRAINT "ase_tipo_poblacions_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.ase_tipo_regimens" (
	"id" int NOT NULL,
	"descripcion" character varying NOT NULL UNIQUE,
	CONSTRAINT "ase_tipo_regimens_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.pqr_tipo_solicitud_especificas" (
	"id" int NOT NULL,
	"descripcion" character varying NOT NULL UNIQUE,
	CONSTRAINT "pqr_tipo_solicitud_especificas_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.glb_barrios_veredas" (
	"id" int NOT NULL,
	"descripcion" character varying NOT NULL UNIQUE,
	"glb_comunas_corregimiento_id" int NOT NULL,
	CONSTRAINT "glb_barrios_veredas_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.glb_comunas_corregimientos" (
	"id" int NOT NULL,
	"descripcion" character varying NOT NULL UNIQUE,
	"glb_zona_id" bigint NOT NULL,
	CONSTRAINT "glb_comunas_corregimientos_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.glb_zona" (
	"id" int NOT NULL,
	"descripcion" character varying NOT NULL UNIQUE,
	CONSTRAINT "glb_zona_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.glb_tipo_identificacions" (
	"id" int NOT NULL,
	"sigla" character varying NOT NULL UNIQUE,
	"descripcion" character varying NOT NULL UNIQUE,
	CONSTRAINT "glb_tipo_identificacions_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.glb_entidads" (
	"id" int NOT NULL,
	"codigo_entidad" character varying NOT NULL UNIQUE,
	"glb_tipo_identificacion_id" int NOT NULL,
	"identificacion" character varying NOT NULL UNIQUE,
	"razon_social" character varying NOT NULL UNIQUE,
	"direccion" character varying NOT NULL,
	CONSTRAINT "glb_entidads_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "pqr_radicacions" ADD CONSTRAINT "pqr_radicacions_fk0" FOREIGN KEY ("glb_estado_id") REFERENCES "glb_estados"("id");
ALTER TABLE "pqr_radicacions" ADD CONSTRAINT "pqr_radicacions_fk1" FOREIGN KEY ("glb_dependencia_id") REFERENCES "glb_dependencias"("id");
ALTER TABLE "pqr_radicacions" ADD CONSTRAINT "pqr_radicacions_fk2" FOREIGN KEY ("pqr_derechos_id") REFERENCES "pqr_tipo_derechos"("id");
ALTER TABLE "pqr_radicacions" ADD CONSTRAINT "pqr_radicacions_fk3" FOREIGN KEY ("ase_tipo_poblacion_id") REFERENCES "ase_tipo_poblacions"("id");
ALTER TABLE "pqr_radicacions" ADD CONSTRAINT "pqr_radicacions_fk4" FOREIGN KEY ("ase_tipo_regimen_id") REFERENCES "ase_tipo_regimens"("id");
ALTER TABLE "pqr_radicacions" ADD CONSTRAINT "pqr_radicacions_fk5" FOREIGN KEY ("pqr_tipo_solicitud_id") REFERENCES "pqr_tipo_solicituds"("id");
ALTER TABLE "pqr_radicacions" ADD CONSTRAINT "pqr_radicacions_fk6" FOREIGN KEY ("pqr_tipo_solicitud_especifica_id") REFERENCES "pqr_tipo_solicitud_especificas"("id");
ALTER TABLE "pqr_radicacions" ADD CONSTRAINT "pqr_radicacions_fk7" FOREIGN KEY ("glb_barrio_vereda") REFERENCES "glb_barrios_veredas"("id");
ALTER TABLE "pqr_radicacions" ADD CONSTRAINT "pqr_radicacions_fk8" FOREIGN KEY ("glb_tipo_identificacion_id") REFERENCES "glb_tipo_identificacions"("id");








ALTER TABLE "glb_barrios_veredas" ADD CONSTRAINT "glb_barrios_veredas_fk0" FOREIGN KEY ("glb_comunas_corregimiento_id") REFERENCES "glb_comunas_corregimientos"("id");

ALTER TABLE "glb_comunas_corregimientos" ADD CONSTRAINT "glb_comunas_corregimientos_fk0" FOREIGN KEY ("glb_zona_id") REFERENCES "glb_zona"("id");



ALTER TABLE "glb_entidads" ADD CONSTRAINT "glb_entidads_fk0" FOREIGN KEY ("glb_tipo_identificacion_id") REFERENCES "glb_tipo_identificacions"("id");











