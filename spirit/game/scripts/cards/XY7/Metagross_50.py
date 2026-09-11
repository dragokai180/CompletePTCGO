from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='635784b6-9b71-54ef-81c3-0d435eba9de5',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name',
    display_name='Metagross',
    searchable_by=['Metagross', 'Stage 2', 'Metagross'],
    subtypes=['Stage 2'],
    collector_number=50,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name',
    family_id=374,
    abilities=[
        Attack(
            title='Machine Gun Stomp',
            game_text='This attack does 10 more damage for each card in your hand.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Guard Press',
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('This Pokémon may have up to 2 Pokémon Tool cards attached to it.'),
)
