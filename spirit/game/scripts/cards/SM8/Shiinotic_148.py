from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='feaba974-af2a-55a7-b5f7-daeaf4a7814d',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shiinotic.Name',
    display_name='Shiinotic',
    searchable_by=['Shiinotic', 'Stage 1', 'Shiinotic'],
    subtypes=['Stage 1'],
    collector_number=148,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name',
    family_id=755,
    abilities=[
        Ability(
            title='Effect Spore',
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Asleep.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Asleep."),
        ),
        Attack(
            title="Dream's Touch",
            game_text="If your opponent's Active Pokémon is Asleep, your opponent shuffles all Energy from it into their deck.",
            cost={PokemonTypes.FAIRY: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
