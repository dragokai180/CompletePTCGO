from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="374fa6ee-9290-59ba-80f8-85e09ced17cc",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Genesect.Name",
    display_name="Genesect",
    searchable_by=["Genesect","Basic","Genesect"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Gaia Blaster",
            game_text="Does 20 more damage for each Grass Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
