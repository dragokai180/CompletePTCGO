from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b127d504-94eb-5e27-9f09-2a11e6bf7a02',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Espathra.Name',
    display_name='Espathra',
    searchable_by=['Espathra', 'Stage 1', 'Espathra'],
    subtypes=['Stage 1'],
    collector_number=103,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name',
    family_id=955,
    abilities=[
        Attack(
            title='Eye Strength',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Psychic',
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
