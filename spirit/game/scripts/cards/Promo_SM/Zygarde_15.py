from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d3a9fc41-9a8f-5c67-8385-dcb05d21799c',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name',
    display_name='Zygarde',
    searchable_by=['Zygarde', 'Basic', 'Zygarde'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=718,
    abilities=[
        Attack(
            title='Pulse Blast',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Land's Wrath",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
