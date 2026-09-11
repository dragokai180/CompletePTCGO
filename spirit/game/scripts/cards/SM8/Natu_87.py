from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='55a88945-967f-5b26-ae16-eb0e95392a35',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name',
    display_name='Natu',
    searchable_by=['Natu', 'Basic', 'Natu'],
    subtypes=['Basic'],
    collector_number=87,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=177,
    abilities=[
        Attack(
            title='Lost March',
            game_text='This attack does 20 damage for each of your Pokémon, except ◇ (Prism Star) Pokémon, in the Lost Zone.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
