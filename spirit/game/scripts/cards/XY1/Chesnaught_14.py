from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f34bbe2e-661f-5d77-a20b-34c30e8d55f1',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chesnaught.Name',
    display_name='Chesnaught',
    searchable_by=['Chesnaught', 'Stage 2', 'Chesnaught'],
    subtypes=['Stage 2'],
    collector_number=14,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Quilladin.Name',
    family_id=650,
    abilities=[
        Ability(
            title='Spiky Shield',
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon."),
        ),
        Attack(
            title='Touchdown',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
