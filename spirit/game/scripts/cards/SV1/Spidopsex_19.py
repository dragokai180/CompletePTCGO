from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='94c556d0-70be-5ee0-8ffd-df10b0152d8e',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spidopsex.Name',
    display_name='Spidops ex',
    searchable_by=['Spidops ex', 'Stage 1', 'ex', 'Spidopsex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=19,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name',
    family_id=917,
    abilities=[
        Ability(
            title='Trap Territory',
            game_text="Your opponent's Active Pokémon's Retreat Cost is Colorless more.",
            passive=standard_passive("Your opponent's Active Pokémon's Retreat Cost is Colorless more."),
        ),
        Attack(
            title='Wire Hang',
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
