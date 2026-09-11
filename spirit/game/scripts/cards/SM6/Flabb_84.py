from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0fc4bb96-0d3a-5359-84bb-4ff9a78da586',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name',
    display_name='Flabébé',
    searchable_by=['Flabébé', 'Basic', 'Flabb'],
    subtypes=['Basic'],
    collector_number=84,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=669,
    abilities=[
        Attack(
            title='Secret Blessings',
            game_text='Shuffle 3 in any combination of Pokémon and basic Energy cards from your discard pile into your deck.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
    ],
)
