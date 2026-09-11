from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import DriftingBalloonPassive, derail
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="4ee22711-f4ff-5f07-9371-f62b61922b53",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyuremEX.Name",
    display_name="Kyurem-EX",
    searchable_by=["Kyurem-EX","Basic","EX","KyuremEX"],
    subtypes=["Basic","EX"],
    collector_number=37,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    abilities=[
        Attack(
            title="Frozen Wings",
            game_text="Discard a Special Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=derail,
        ),
        Attack(
            title="Hail Blizzard",
            game_text="This Pokémon can't use Hail Blizzard during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=bw_legacy_attack,
        ),
    ],
)
