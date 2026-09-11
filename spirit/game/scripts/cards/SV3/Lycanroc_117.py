from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='baaf563a-a123-5355-904a-408348ea30be',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name',
    display_name='Lycanroc',
    searchable_by=['Lycanroc', 'Stage 1', 'Lycanroc'],
    subtypes=['Stage 1'],
    collector_number=117,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name',
    family_id=744,
    abilities=[
        Attack(
            title='Finishing Fang',
            game_text="If your opponent's Active Pokémon has no damage counters on it before this attack does damage, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=90,
            effect=standard_attack,
        ),
        Attack(
            title='Slashing Claw',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
