from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a0572058-9cf8-51f1-84b3-d61aa5ad8706',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwoex.Name',
    display_name='Mewtwo ex',
    searchable_by=['Mewtwo ex', 'Basic', 'ex', 'Mewtwoex'],
    subtypes=['Basic', 'ex'],
    collector_number=64,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=150,
    abilities=[
        Attack(
            title='Photon Bullets',
            game_text="This attack does 50 damage to each of your opponent's Pokémon ex. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Psychic Powers',
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=230,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
