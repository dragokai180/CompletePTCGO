from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7abc8a3d-aba6-5abf-8fb6-a4939b4686d0',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name',
    display_name='Hoothoot',
    searchable_by=['Hoothoot', 'Basic', 'Hoothoot'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'HGSS05'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=163,
    abilities=[
        Ability(
            title='Insomnia',
            game_text="Hoothoot can't be Asleep.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("Hoothoot can't be Asleep."),
        ),
        Attack(
            title='Peck',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
