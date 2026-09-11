from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d98d6d80-dcc4-523f-b673-17385ca0c634',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name',
    display_name='Bronzong',
    searchable_by=['Bronzong', 'Stage 1', 'Bronzong'],
    subtypes=['Stage 1'],
    collector_number=101,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name',
    family_id=436,
    abilities=[
        Ability(
            title='Heatproof',
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Fire Pokémon.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from your opponent's Fire Pokémon."),
        ),
        Attack(
            title='Shady Stamp',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
