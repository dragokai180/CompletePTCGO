from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per

card = PokemonCardDef(
    guid="5460df38-dd19-535b-b374-faa3df375bad",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaMeganiumex.Name",
    display_name="Mega Meganium ex",
    searchable_by=["Mega Meganium ex","Stage 2","ex","SV_Mega","MegaMeganiumex"],
    subtypes=["Stage 2","ex","SV_Mega"],
    collector_number=10,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=360,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    family_id=152,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    abilities=[
        Attack(
            title="Giant Bouquet",
            game_text="This attack does 50 more damage for each Grass Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=damage_per(
                count_energy("self", energy_type=PokemonTypes.GRASS), 50, base=70,
            ),
        ),
    ],
)
