from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0a978d01-a2cf-5726-b858-78c26ab947aa',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name',
    display_name='Zacian',
    searchable_by=['Zacian', 'Basic', 'Zacian'],
    subtypes=['Basic'],
    collector_number=136,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=888,
    abilities=[
        Attack(
            title='Iron Roar',
            game_text='Attach a Basic Metal Energy card from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Brave Blade',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
