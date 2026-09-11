from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='207eb06d-7d65-5de1-a084-16aa2e76cf25',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name',
    display_name='Bronzor',
    searchable_by=['Bronzor', 'Basic', 'Bronzor'],
    subtypes=['Basic'],
    collector_number=100,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=436,
    abilities=[
        Ability(
            title='Evolutionary Advantage',
            game_text='If you go second, this Pokémon can evolve during your first turn.',
            passive=standard_passive('If you go second, this Pokémon can evolve during your first turn.'),
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
