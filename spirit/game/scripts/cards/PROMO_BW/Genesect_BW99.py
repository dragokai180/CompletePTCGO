from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import destructive_beam
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="1b8a3fd0-0d0d-5f38-b9af-b8cd0b45d580",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Genesect.Name",
    display_name="Genesect",
    searchable_by=["Genesect","Basic","Genesect"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=destructive_beam,
        ),
        Attack(
            title="Breaker Bazooka",
            game_text="Discard all Grass Energy attached to this Pokémon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=bw_legacy_attack,
        ),
    ],
)
