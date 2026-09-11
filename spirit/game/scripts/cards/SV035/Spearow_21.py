from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5834c9d4-6487-57c4-8d1b-39c891e2b46d',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name',
    display_name='Spearow',
    searchable_by=['Spearow', 'Basic', 'Spearow'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=21,
    abilities=[
        Ability(
            title='Evolutionary Advantage',
            game_text='If you go second, this Pokémon can evolve during your first turn.',
            passive=standard_passive('If you go second, this Pokémon can evolve during your first turn.'),
        ),
        Attack(
            title='Speed Dive',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
