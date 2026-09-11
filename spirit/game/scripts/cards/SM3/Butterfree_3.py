from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='400314cf-bcf5-532b-b723-2bae6a488e12',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name',
    display_name='Butterfree',
    searchable_by=['Butterfree', 'Stage 2', 'Butterfree'],
    subtypes=['Stage 2'],
    collector_number=3,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name',
    family_id=10,
    abilities=[
        Attack(
            title='Bye-Bye Heal',
            game_text='Heal all damage from all of your Pokémon. Shuffle this Pokémon and all cards attached to it into your deck.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Stun Spore',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
