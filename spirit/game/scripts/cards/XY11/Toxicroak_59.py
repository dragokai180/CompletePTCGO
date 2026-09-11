from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7508a80b-3870-5183-adeb-5b04c624dd4b',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name',
    display_name='Toxicroak',
    searchable_by=['Toxicroak', 'Stage 1', 'Toxicroak'],
    subtypes=['Stage 1'],
    collector_number=59,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name',
    family_id=453,
    abilities=[
        Ability(
            title='Poison Enzyme',
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Poisoned Pokémon.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from your opponent's Poisoned Pokémon."),
        ),
        Attack(
            title='Poison Jab',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
