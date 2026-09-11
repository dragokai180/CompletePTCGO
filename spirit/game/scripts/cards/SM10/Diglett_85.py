from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ddc7579d-839f-58e3-ba41-3267bea5d941',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name',
    display_name='Diglett',
    searchable_by=['Diglett', 'Basic', 'Diglett'],
    subtypes=['Basic'],
    collector_number=85,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=50,
    abilities=[
        Ability(
            title='Underground Work',
            game_text="If you discard this Pokémon with the effect of Giovanni's Exile, discard the top card of your opponent's deck.",
            passive=standard_passive("If you discard this Pokémon with the effect of Giovanni's Exile, discard the top card of your opponent's deck."),
        ),
        Attack(
            title='Hook',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
