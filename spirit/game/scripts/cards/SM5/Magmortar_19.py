from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='679f52f2-3f31-550a-918b-c0604261ed3b',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name',
    display_name='Magmortar',
    searchable_by=['Magmortar', 'Stage 1', 'Magmortar'],
    subtypes=['Stage 1'],
    collector_number=19,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name',
    family_id=126,
    abilities=[
        Ability(
            title='Incandescent Body',
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Burned.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Burned."),
        ),
        Attack(
            title='Fire Blaster',
            game_text='You may discard 2 Energy from this Pokémon. If you do, this attack does 80 more damage.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
