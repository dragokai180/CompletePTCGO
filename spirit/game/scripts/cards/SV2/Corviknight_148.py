from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='722c3d6d-f4c8-579f-8031-c1f79321d248',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Corviknight.Name',
    display_name='Corviknight',
    searchable_by=['Corviknight', 'Stage 2', 'Corviknight'],
    subtypes=['Stage 2'],
    collector_number=148,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Corvisquire.Name',
    family_id=821,
    abilities=[
        Attack(
            title='Accelerate',
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.METAL: 1},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Spinning Bird',
            game_text='Discard 2 Energy from this Pokémon.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
