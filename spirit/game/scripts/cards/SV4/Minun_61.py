from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9ad2de70-83a2-5c6b-a511-6beea227a7a9',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name',
    display_name='Minun',
    searchable_by=['Minun', 'Basic', 'Minun'],
    subtypes=['Basic'],
    collector_number=61,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=312,
    abilities=[
        Ability(
            title='Buddy Pulse',
            game_text="If you have Plusle in play, whenever your opponent attaches an Energy card from their hand to 1 of their Pokémon, put 2 damage counters on that Pokémon. The effect of Buddy Pulse doesn't stack.",
            effect=standard_ability,
            trigger=Triggers.ON_ENERGY_ATTACHED,
        ),
        Attack(
            title='Speed Ball',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)
