from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3a41277-eae8-5eae-9759-41cec43457ed',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Granbull.Name',
    display_name='Granbull',
    searchable_by=['Granbull', 'Stage 1', 'Granbull'],
    subtypes=['Stage 1'],
    collector_number=91,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name',
    family_id=209,
    abilities=[
        Attack(
            title='Dark Clamp',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Fight Back',
            game_text='If this Pokémon has any damage counters on it, this attack does 80 more damage.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
