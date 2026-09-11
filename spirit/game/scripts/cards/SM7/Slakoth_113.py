from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='068bbc61-2eb7-50f8-914e-90ca490ef74b',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name',
    display_name='Slakoth',
    searchable_by=['Slakoth', 'Basic', 'Slakoth'],
    subtypes=['Basic'],
    collector_number=113,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=287,
    abilities=[
        Attack(
            title='Claw',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Slack Off',
            game_text="Heal all damage from this Pokémon. It can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
