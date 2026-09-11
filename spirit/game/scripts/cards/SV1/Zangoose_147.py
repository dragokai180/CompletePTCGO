from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6f907496-8da7-5f06-bd85-9dab7ecc82a3',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name',
    display_name='Zangoose',
    searchable_by=['Zangoose', 'Basic', 'Zangoose'],
    subtypes=['Basic'],
    collector_number=147,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=335,
    abilities=[
        Attack(
            title='Drag Off',
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot. This attack does 30 damage to the new Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Slashing Claw',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
