from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='09e05357-b17a-5abc-a537-0aec6c5dd546',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name',
    display_name='Sableye',
    searchable_by=['Sableye', 'Basic', 'Sableye'],
    subtypes=['Basic'],
    collector_number=80,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=302,
    abilities=[
        Attack(
            title='Limitation',
            game_text="Your opponent can't play any Supporter cards from their hand during their next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Scratch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
