from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='12199818-bb00-51c0-8685-4b63ad3ffa50',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellibolt.Name',
    display_name='Bellibolt',
    searchable_by=['Bellibolt', 'Stage 1', 'Bellibolt'],
    subtypes=['Stage 1'],
    collector_number=78,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name',
    family_id=938,
    abilities=[
        Ability(
            title='Insulator',
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Lightning Pokémon.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from your opponent's Lightning Pokémon."),
        ),
        Attack(
            title='Thunderous Edge',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
