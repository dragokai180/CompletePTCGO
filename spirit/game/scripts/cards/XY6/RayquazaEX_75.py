from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d8a4d79-2dea-59e4-a6c2-a27d7cb9dacd',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name',
    display_name='Rayquaza-EX',
    searchable_by=['Rayquaza-EX', 'Basic', 'EX', 'RayquazaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=75,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=384,
    abilities=[
        Attack(
            title='Intensifying Burn',
            game_text="If your opponent's Active Pokémon is a Pokémon-EX, this attack does 50 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Pulse',
            game_text='Discard the top 3 cards of your deck.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
