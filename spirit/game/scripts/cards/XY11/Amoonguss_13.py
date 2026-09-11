from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3059cb29-cc3c-53ee-af6b-4dd7d027d37e',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name',
    display_name='Amoonguss',
    searchable_by=['Amoonguss', 'Stage 1', 'Amoonguss'],
    subtypes=['Stage 1'],
    collector_number=13,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name',
    family_id=590,
    abilities=[
        Attack(
            title='Crazy Spore',
            game_text="Your opponent's Active Pokémon is now Confused and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Strange Reaction',
            game_text="If your opponent's Active Pokémon is Confused, it is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
