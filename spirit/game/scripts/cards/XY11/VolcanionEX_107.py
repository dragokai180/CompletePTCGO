from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.standard_era import steam_up, steam_up_condition


card = PokemonCardDef(
    guid='cf9d1f51-1448-5249-9464-4d7992fa5068',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.VolcanionEX.Name',
    display_name='Volcanion-EX',
    searchable_by=['Volcanion-EX', 'Basic', 'EX', 'VolcanionEX'],
    subtypes=['Basic', 'EX'],
    collector_number=107,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIRE, PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=721,
    abilities=[
        Ability(
            title='Steam Up',
            game_text="Once during your turn (before your attack), you may discard a Fire Energy card from your hand. If you do, during this turn, your Basic Fire Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            effect=steam_up,
            condition=steam_up_condition,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Volcanic Heat',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
