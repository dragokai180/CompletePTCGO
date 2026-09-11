from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="38302287-4728-529d-92e8-6ef454d17735",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CelebiEX.Name",
    display_name="Celebi-EX",
    searchable_by=["Celebi-EX","Basic","EX","CelebiEX"],
    subtypes=["Basic","EX"],
    collector_number=9,
    set_code="BW7",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    abilities=[
        Ability(
            title="Time Recall",
            game_text="Each of your evolved Pokémon can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)",
            passive=bw_legacy_passive("Each of your evolved Pokémon can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)"),
        ),
        Attack(
            title="Wind Whisk",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=switch_self_attack(),
        ),
    ],
)
