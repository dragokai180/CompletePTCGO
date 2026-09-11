from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b0a62d74-81b4-5540-8085-5658a16be821',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name',
    display_name='Floette',
    searchable_by=['Floette', 'Stage 1', 'Floette'],
    subtypes=['Stage 1'],
    collector_number=85,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name',
    family_id=669,
    abilities=[
        Attack(
            title='Swirling Petals',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. If you do, switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
    ],
)
