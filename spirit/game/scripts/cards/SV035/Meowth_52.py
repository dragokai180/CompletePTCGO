from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e5af1681-4286-58cb-a99a-c89eb68392ba',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name',
    display_name='Meowth',
    searchable_by=['Meowth', 'Basic', 'Meowth'],
    subtypes=['Basic'],
    collector_number=52,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=52,
    abilities=[
        Attack(
            title='Come Here Right Meow',
            game_text="Flip a coin. If heads, switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dig Claws',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
