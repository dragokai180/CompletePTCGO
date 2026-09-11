from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import DriftingBalloonPassive, derail
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="83b30668-912e-56b6-8bad-4ba31b49d72e",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CobalionEX.Name",
    display_name="Cobalion-EX",
    searchable_by=["Cobalion-EX","Basic","EX","CobalionEX"],
    subtypes=["Basic","EX"],
    collector_number=93,
    set_code="BW8",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Righteous Edge",
            game_text="Discard a Special Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=derail,
        ),
        Attack(
            title="Steel Bullet",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on the Defending Pokémon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=bw_legacy_attack,
        ),
    ],
)
