from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='02dc5906-c2fc-5af2-ac91-520cf6cc21c3',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name',
    display_name='Krookodile',
    searchable_by=['Krookodile', 'Stage 2', 'Krookodile'],
    subtypes=['Stage 2'],
    collector_number=117,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name',
    family_id=551,
    abilities=[
        Attack(
            title='Chomp Chomp Bite',
            game_text="Flip a coin until you get tails. For each heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Earthquake',
            game_text="This attack also does 30 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
