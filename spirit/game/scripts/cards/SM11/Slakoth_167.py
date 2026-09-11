from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7edf8df3-db60-5fa4-a2b4-1bf5ed0cfa34',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name',
    display_name='Slakoth',
    searchable_by=['Slakoth', 'Basic', 'Slakoth'],
    subtypes=['Basic'],
    collector_number=167,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=287,
    abilities=[
        Attack(
            title='Lazy Howl',
            game_text="During your opponent's next turn, if they attach an Energy card from their hand to the Defending Pokémon, their turn ends.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hang Down',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
