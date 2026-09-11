from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='888a34f9-e88e-5cc5-8217-608e4028db7d',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name',
    display_name='Flabébé',
    searchable_by=['Flabébé', 'Basic', 'Flabb'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=669,
    abilities=[
        Ability(
            title='Evolutionary Advantage',
            game_text='If you go second, this Pokémon can evolve during your first turn.',
            passive=standard_passive('If you go second, this Pokémon can evolve during your first turn.'),
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
        ),
    ],
)
