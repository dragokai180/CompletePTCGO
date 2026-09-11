from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8dcfaed6-46e6-501f-9081-02d627e3db2d',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name',
    display_name='Sharpedo',
    searchable_by=['Sharpedo', 'Stage 1', 'Sharpedo'],
    subtypes=['Stage 1'],
    collector_number=82,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name',
    family_id=318,
    abilities=[
        Ability(
            title='Rough Skin',
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon."),
        ),
        Attack(
            title='Aqua Impact',
            game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
