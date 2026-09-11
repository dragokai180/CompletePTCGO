from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d50293e8-65c3-54ca-b94b-ca127dce85ca',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name',
    display_name='Ditto',
    searchable_by=['Ditto', 'Basic', 'Ditto'],
    subtypes=['Basic'],
    collector_number=17,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=132,
    abilities=[
        Ability(
            title='Dittobolic',
            game_text='The number of Benched Pokémon your opponent can have is now 4. If your opponent has 5 Benched Pokémon, your opponent must discard 1 of them and all cards attached to it.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('The number of Benched Pokémon your opponent can have is now 4. If your opponent has 5 Benched Pokémon, your opponent must discard 1 of them and all cards attached to it.'),
        ),
        Attack(
            title='Sharp Point',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
