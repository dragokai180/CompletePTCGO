from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d39573d3-372f-5739-a302-9eaa257cd1ba',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name',
    display_name='Bewear',
    searchable_by=['Bewear', 'Stage 1', 'Bewear'],
    subtypes=['Stage 1'],
    collector_number=56,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name',
    family_id=759,
    abilities=[
        Ability(
            title='Fluffy',
            game_text="This Pokémon takes 30 less damage from the attacks of your opponent's non-Fire Pokémon (after applying Weakness and Resistance).",
            passive=standard_passive("This Pokémon takes 30 less damage from the attacks of your opponent's non-Fire Pokémon (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Cross-Cut',
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
