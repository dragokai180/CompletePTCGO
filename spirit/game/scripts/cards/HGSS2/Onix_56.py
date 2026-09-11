from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cddd0f8d-49c1-57d2-b46c-8e5172fb6de3',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name',
    display_name='Onix',
    searchable_by=['Onix', 'Basic', 'Onix'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=95,
    abilities=[
        Ability(
            title='Energy Healer',
            game_text='Whenever you attach an Energy card from your hand to Onix, remove a damage counter from Onix.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('Whenever you attach an Energy card from your hand to Onix, remove a damage counter from Onix.'),
        ),
        Attack(
            title='Boundless Power',
            game_text="Onix can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
