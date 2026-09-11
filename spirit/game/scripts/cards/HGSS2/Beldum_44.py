from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9700132f-a66f-5875-bac0-bd20a89a7a80',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name',
    display_name='Beldum',
    searchable_by=['Beldum', 'Basic', 'Beldum'],
    subtypes=['Basic'],
    collector_number=44,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=374,
    abilities=[
        Attack(
            title='Reaction',
            game_text='You may switch Beldum with 1 of your Benched Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
