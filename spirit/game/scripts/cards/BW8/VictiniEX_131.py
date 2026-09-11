from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="44a957de-5afe-50da-b2c9-6efef376de54",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniEX.Name",
    display_name="Victini-EX",
    searchable_by=["Victini-EX","Basic","EX","VictiniEX"],
    subtypes=["Basic","EX"],
    collector_number=131,
    set_code="BW8",
    rarity=Rarities.RareUltra,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Turbo Energize",
            game_text="Search your deck for 2 basic Energy cards and attach them to your Benched Pokémon in any way you like. Shuffle your deck afterward.",
            cost={PokemonTypes.FIRE: 1},
            effect=search_attach_energy(is_basic_energy_card, count=2),
        ),
        Attack(
            title="Intensifying Burn",
            game_text="If the Defending Pokémon is a Pokémon-EX, this attack does 50 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
