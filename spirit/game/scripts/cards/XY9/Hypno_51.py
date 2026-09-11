from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
    goodnight_babies,
)


card = PokemonCardDef(
    guid='326f178e-93e8-5403-bcd0-778cc7c1e51e',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name',
    display_name='Hypno',
    searchable_by=['Hypno', 'Stage 1', 'Hypno'],
    subtypes=['Stage 1'],
    collector_number=51,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name',
    family_id=96,
    abilities=[
        Ability(
            title='Goodnight, Babies',
            game_text='Once during your turn (before your attack), you may leave both Active Pokémon Asleep.',
            effect=goodnight_babies,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Zen Headbutt',
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
        ),
    ],
)
