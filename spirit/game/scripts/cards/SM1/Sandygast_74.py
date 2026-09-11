from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bafce824-63b7-55d7-a02b-1ad280869863',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name',
    display_name='Sandygast',
    searchable_by=['Sandygast', 'Basic', 'Sandygast'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=769,
    abilities=[
        Attack(
            title='Shore Up',
            game_text='Attach a Fighting Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sand Tomb',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
