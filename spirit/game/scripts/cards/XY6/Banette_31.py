from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0f8c2718-cfcd-59f6-9d70-e9752c630bb3',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name',
    display_name='Banette',
    searchable_by=['Banette', 'Stage 1', 'Banette'],
    subtypes=['Stage 1'],
    collector_number=31,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name',
    family_id=353,
    abilities=[
        Ability(
            title='Tool Concealment',
            game_text='Each Pokémon Tool card in play has no effect.',
            passive=standard_passive('Each Pokémon Tool card in play has no effect.'),
        ),
        Attack(
            title='Psyshot',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
