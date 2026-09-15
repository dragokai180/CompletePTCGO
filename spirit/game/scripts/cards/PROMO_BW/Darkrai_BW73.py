from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive
from spirit.game.card_effects.bw10 import dimension_heal, strafe

card = PokemonCardDef(
    guid="9cfc646b-ab78-5d10-9fde-fbda9927697c",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    display_name="Darkrai",
    searchable_by=["Darkrai","Basic","Darkrai","Team Plasma"],
    subtypes=["Basic","Team Plasma"],
    collector_number=73,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Hide in Shadows",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=strafe,
        ),
        Attack(
            title="Dark Hole",
            game_text="Flip a coin. If heads, the Defending Pokémon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
