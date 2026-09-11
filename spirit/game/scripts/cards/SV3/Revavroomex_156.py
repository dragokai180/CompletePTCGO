from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='30f47760-ae76-579b-904d-a2d82f145fa9',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Revavroomex.Name',
    display_name='Revavroom ex',
    searchable_by=['Revavroom ex', 'Stage 1', 'ex', 'Revavroomex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=156,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name',
    family_id=965,
    abilities=[
        Ability(
            title='Tune-Up',
            game_text='This Pokémon may have up to 4 Pokémon Tools attached to it. If it loses this Ability, discard Pokémon Tools from it until only 1 remains.',
            passive=standard_passive('This Pokémon may have up to 4 Pokémon Tools attached to it. If it loses this Ability, discard Pokémon Tools from it until only 1 remains.'),
        ),
        Attack(
            title='Wild Drift',
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
