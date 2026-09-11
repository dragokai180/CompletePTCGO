from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9320673a-0f92-59b9-be69-661b4d61ef63',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gallade.Name',
    display_name='Gallade',
    searchable_by=['Gallade', 'Stage 2', 'Gallade'],
    subtypes=['Stage 2'],
    collector_number=82,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name',
    family_id=280,
    abilities=[
        Ability(
            title='Double Type',
            game_text='As long as this Pokémon is in play, it is Psychic and Fighting type.',
            passive=standard_passive('As long as this Pokémon is in play, it is Psychic and Fighting type.'),
        ),
        Attack(
            title='Power Cyclone',
            game_text='Move an Energy from this Pokémon to 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
